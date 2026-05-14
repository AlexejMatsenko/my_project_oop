from unittest.mock import patch, mock_open

from src.utils import object_from_json
from src.utils import read_json


@patch("builtins.open", new_callable=mock_open, read_data="[1, 2, 3]")
@patch("json.load")
def test_read_json_file(mock_json_load, mock_open):
    mock_json_load.return_value = [1, 2, 3]
    result = read_json("fake_file.json")
    assert result == [1, 2, 3]
    mock_open.assert_called_once_with("fake_file.json", "r", encoding="UTF-8")
    mock_json_load.assert_called_once()


def test_object_json(object_json):
    result = object_from_json(object_json)
    assert len(result) == 1

    assert result[0].name == "Смартфоны"
    # assert result[0]. == "Samsung Galaxy C23 Ultra"
