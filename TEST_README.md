# Testing Strategy

## Unit Tests

- Followed a **modular approach**, ensuring that each function and class was tested in isolation.
- Used **pytest** as the primary testing framework for concise and readable test cases.
- Each test focused on a **single behavior**, making it easy to pinpoint failures.
- Used **mocking and patching** (via `unittest.mock`) to isolate components and avoid external dependencies.
- **Async test support**: Used `pytest.mark.asyncio` to handle asynchronous functions.
- **Parameterized tests**: Used `pytest.mark.parametrize` to efficiently test multiple input scenarios.

## Integration Tests

- Used `httpx.AsyncClient` to test API endpoints in an **asynchronous** environment.
- Verified full **request-response cycles**, including authentication handling.
- Mocked **database interactions** using fixtures and dependency injection to simulate real-world scenarios.
- Ensured proper **cleanup and state management** using `pytest` fixtures.

## Ensuring Reliability and Maintainability

- **Consistent Test Naming**: Used clear and descriptive test names (`test_functionality_scenario` format).
- **Continuous Integration (CI)**: Integrated tests into **GitHub Actions CI/CD**, ensuring tests run on each commit.
- **Code Coverage Metrics**: Enforced high test coverage using `pytest-cov` to detect untested parts of the code.
- **Reusable Fixtures**: Defined reusable test setups in `conftest.py`, including authentication tokens and database connections.
- **Minimal External Dependencies**: Used mocks where necessary to avoid reliance on external services.
- **Regular Refactoring**: Kept tests updated as the codebase evolved to prevent test rot.

## Challenges and Solutions

### 1. Handling External Dependencies in Tests
**Solution:** Used `unittest.mock` to mock APIs, databases, and file operations, ensuring tests ran in isolation.

### 2. Testing Asynchronous Code
**Solution:** Used `pytest.mark.asyncio` to properly handle async test functions and avoid event loop issues.

### 3. API Testing with Authentication
**Solution:** Implemented `AsyncClient` with authentication headers to test secured endpoints.

## Running Tests Locally

### Prerequisites

1. Ensure you have Python 3.9 above  installed.
2. Install dependencies using:
   ```bash
   pip install -r requirements.txt
   ```
3. Navigate to the project directory:

    ```bash
    cd bookstore
    ```

### Running Tests


#### Before running tests for Api's testing run below command to run main.py ,which will run in http://127.0.0.1:8000

```bash
  uvicorn main:app --reload
```


#### Run test coverage from bookstore which will give coverage in terminal
```bash
  pytest --cov=bookstore tests/
```

#### To generate a detailed test coverage report in HTML format, run:
This command runs all tests and generates a coverage report in an htmlcov/directory.
Index.html report visually highlights which lines of code are tested and which are not tested.
```bash
  pytest --cov=bookstore  --cov-report=html tests/
```

#### Run api integration tests from bookstore 
```bash
  pytest tests/test_integration_api.py
```

#### To test db related testing
```bash
  pytest tests/test_mock_db.py
```

#### To test credentials related testing
```bash
  pytest tests/test_credentials.py
```

---

### Notes
- Test results and **coverage reports** are generated automatically in **CI/CD pipeline**.
- The **coverage report** can be downloaded from:
  GitHub Actions → Workflow Run → Artifacts section → at bottom of the page `coverage-report`