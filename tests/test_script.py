from unittest.mock import Mock, patch

from src.script import get_tips, TIPS_URL


@patch('requests.get')
def test_get_tips(mock_get, tips):
    mock_get.return_value = Mock(
        status_code=200,
        json=lambda: tips
    )
    tips = get_tips()
    assert len(tips) == 3
    actual = [tip['title'] for tip in tips]
    expected = ['make a dict using zip',
                'split a string into a list',
                'swap 2 variables']
    assert actual == expected


@patch('requests.get')
def test_wrong_url(mock_get):
    mock_get.return_value = Mock(
        status_code=404,
        json=[]
    )
    tips = get_tips(TIPS_URL.replace('tips/', 'tipssss/'))
    assert tips == []
