# Conformity Assessment Policy and Credential Profile ontology

This repository contains the ontology - schema and shapes - files related to the conformity assessment.

The main website is located [here](https://eclipse-dataspace-cap.github.io/).

The questions / issues about the ontology, use this project [issues](https://github.com/eclipse-dataspace-cap/cap-ontology/issues).

## Contributions

The framework used to build the ontology is [LinkML](https://linkml.io/)


## Development

Python files are formatted with [`ruff`](https://docs.astral.sh/ruff) and the configuration is in `ruff.toml`.

Using [`uv`](https://github.com/astral-sh/uv), you can install the dependencies with

```shell
uv venv
uv pip install -r requirements.txt
```

Using [`act`](https://github.com/nektos/act), you can list possible jobs with `act --list` and run a job with `act -j <job>`

Example:

```shell
act --rm --job build --artifact-server-path artefacts
unzip -o artefacts/1/github-pages/github-pages.zip && tar xfv artifact.tar -C public
python3 -m http.server -d public
# and browse to http://localhost:8000
```

Note: `@semantic-release` asks for write access on the repository, even with `--dry-run`.
You get setup your token access one with [`gh`](https://cli.github.com/).

```shell
brew install gh
gh auth login
echo GITHUB_TOKEN=$(gh auth token) > .env
```
