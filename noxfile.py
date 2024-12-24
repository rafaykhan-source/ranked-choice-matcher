"""The noxfile for the application serves to standardize project tooling."""

import nox

nox.options.sessions = ["lint", "tests"]


@nox.session
def format(session):
    session.install("ruff")
    session.run("ruff", "format", "src")


@nox.session
def lint(session):
    session.install("ruff")
    session.run("ruff", "check", "src", "--fix", "--show-fixes")
    session.notify("format")


@nox.session
def tests(session):
    session.install(".[test]")
    session.run("pytest")


@nox.session
def docs(session):
    del session
