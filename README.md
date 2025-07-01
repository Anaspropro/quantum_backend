# Quantum Circuit Simulator Backend

This is a Django REST API backend for simulating quantum circuits using Qiskit. It is designed to be used with a frontend (such as React or Next.js) for building and visualizing quantum circuits.

## Features
- Simulate quantum circuits with basic gates (H, X, Y, Z, CX/CNOT)
- Returns measurement results and statevector
- Simple, open API (no authentication required)

## Requirements
- Python 3.10+
- Django 5.x
- Django REST Framework
- Qiskit
- Qiskit Aer

## Setup

1. **Clone the repository**

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Apply migrations**
```bash
python manage.py makemigrations
python manage.py migrate
```

4. **Run the development server**
```bash
python manage.py runserver
```

## API Endpoints

### Simulate Quantum Circuit
- **POST** `/api/simulate/`
- **Body:**
  ```json
  {
    "numQubits": 2,
    "circuit": [
      {"gate": "H", "targets": [0]},
      {"gate": "CX", "targets": [0, 1]}
    ]
  }
  ```
- **Response:**
  ```json
  {
    "result": {
      "counts": {"01": 1},
      "statevector": [ ... ]
    }
  }
  ```

## Notes
- Only the simulation endpoint is exposed; there is no authentication or user management.
- For production, add security and authentication as needed.

## License
MIT
