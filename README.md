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
   - `date`: `year`, `month` and `day` params will override relative now + date result if set

## Config examples
Example config for birth year=2001 and always today:
```yaml
api_id: 12345
api_hash: abcd
delta:
  weeks: 0
  days: 0
  hours: 0
date:
  year: 2001
```

Another example to be always 18 y.o. and birthday each month 1st day:
```yaml
api_id: 12345
api_hash: abcd
delta:
  weeks: 0
  days: -6 574 # 365*18+4
  hours: 0
date:
  day: 1
```

## Usage
You can use it in two ways
### Manual
`poetry run python main.py`

On first run you will authorise into you account, after that you can run it without interaction, for example with cron

### CRON
You have to run it manual first time in order to authorise the account

`0 12 * * * cd /path/to/myRelativeBirthday && poetry run python main.py`
