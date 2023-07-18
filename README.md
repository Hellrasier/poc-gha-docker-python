# Simple Python Action
The POC of the minimal GHA (Python) which will be build into a Docker container. 

### Usage
### Example workflow
Passing text parameters to the action:
```yaml
name: CI
...
jobs:
  build:
    ...
      - name: Run Docker action
        uses: zloader/poc-gha-docker-python@main
        with:
          hat-parameters: "eyJuYW1lIjoiVGVzdCIsImFjdGl2ZSI6dHJ1ZX0="
```

Passing artifact(s) to the action:
```yaml
name: CI
...
jobs:
  build:
    ...
      - name: Download artifacts
        uses: actions/download-artifact@v3
        with:
          name: Some reports
          path: reports/

      - name: Run Docker action
        uses: zloader/poc-gha-docker-python@main
        with:
          hat-artifact: "/reports/report.xml"
```