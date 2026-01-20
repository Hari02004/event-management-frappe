### Event Manager

Event Management App

### Installation

You can install this app using the [bench](https://github.com/frappe/bench) CLI:

```bash
cd $PATH_TO_YOUR_BENCH
bench get-app $URL_OF_THIS_REPO --branch develop
bench install-app event_manager
```

### Contributing

This app uses `pre-commit` for code formatting and linting. Please [install pre-commit](https://pre-commit.com/#installation) and enable it for this repository:

```bash
cd apps/event_manager
pre-commit install
```

Pre-commit is configured to use the following tools for checking and formatting your code:

- ruff
- eslint
- prettier
- pyupgrade

### License

mit
# Event Management System (Frappe)

## Features
- Create and manage Events (Events1 DocType)
- Register Attendees linked to Events
- Create Tickets linked to Attendees and Events
- Auto calculation of:
  - Tickets Sold
  - Remaining Capacity
- Capacity validation
- Client Script based automation
- CSV template provided (UI import not available in this Frappe version)

## Tech Stack
- Frappe Framework
- Python
- JavaScript (Client Script)
- MariaDB

## How to Run
1. Install Frappe Bench
2. Clone this repository inside apps folder
3. Run:
   bench start
4. Open browser:
   http://127.0.0.1:8000

## CSV Import
Due to Frappe UI limitations for custom DocTypes, CSV import is not visible in UI.
Sample CSV file is provided for demonstration.

## Author
Hari Krishnan
