# MyRelativeBirthday
A simple script to set your birthday in telegram relative to the current date. Birthday ~~only once a year~~ **everyday**! Just for fun

## Installation
1. Clone the repository
2. Install poetry woth python 3.10 or higher
3. Install depencies:
   `poetry install`
4. Create config.yml:
   - `api_id` and `api_hash` from my.telegram.org
   - `delta`: set delta relative to the current date

## Usage
You can use it in two ways
### Manual
`poetry run python main.py`

On first run you will authorise into you account, after that you can run it without interaction, for example with cron

### CRON
You have to run it manual first time in order to authorise the account

`0 12 * * * cd /path/to/myRelativeBirthday && poetry python main.py`
