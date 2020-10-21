# Selenium InvalidSelectorException Inconsistency

For python client, the selenium exception `InvalidSelectorException` is not raised in expected_conditions as it would be on find_element methods.

This problem happens on the latest version and `4.0.0a6.post2` version

## Requirements
- python3
- Make

## Usage
To generate the virtual environment and download selenium dependency:

`make env_ok` 

To execute the unit tests

`env/bin/python test_selenium.py`

By changing the requirements.txt you can set another selenium version

`selenium==4.0.0a6.post2`
