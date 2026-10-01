"""Read canonical devspec artifacts without duplicating their content in Python."""

from __future__ import annotations

from dataclasses import dataclass
from pathlib import Path
from xml.etree import ElementTree


@dataclass(frozen=True)
class Command:
    name: str
    purpose: str


def canonical_root() -> Path:
    # A built wheel or executable bundles the artifacts. Checking the source tree first let a frozen
    # executable, whose parents[2] is the system temp directory, adopt any unrelated `devspec` folder.
    bundled = Path(__file__).resolve().parent / "_assets" / "devspec"
    if bundled.is_dir():
        return bundled
    source_tree = Path(__file__).resolve().parents[2] / "devspec"
    if (source_tree / "install-manifest.txt").is_file():
        return source_tree
    raise RuntimeError("Canonical devspec artifacts are unavailable")


def workflow_block(text: str) -> str:
    start = text.index("<workflow")
    end = text.index("</workflow>") + len("</workflow>")
    return text[start:end]


def load_commands() -> tuple[Command, ...]:
    commands: list[Command] = []
    for path in sorted((canonical_root() / "contracts").glob("devspec.*.md")):
        workflow = ElementTree.fromstring(workflow_block(path.read_text(encoding="utf-8")))
        command = workflow.attrib["command"]
        commands.append(Command(command.removeprefix("devspec."), workflow.findtext("purpose", default="")))
    return tuple(commands)


def install_files() -> tuple[Path, ...]:
    root = canonical_root()
    manifest = root / "install-manifest.txt"
    patterns = (
        line.strip()
        for line in manifest.read_text(encoding="utf-8").splitlines()
        if line.strip() and not line.startswith("#")
    )
    files = {path for pattern in patterns for path in root.glob(pattern) if path.is_file()}
    return tuple(sorted(files))


COMMANDS = load_commands()
PROTOCOLS = tuple(path.stem for path in sorted((canonical_root() / "protocols").glob("*.xml")))

# Reading order for human-facing command lists. COMMANDS is sorted by filename, which would
# open every listing with changerequest and hide the route the commands actually follow.
LIFECYCLE_ORDER = (
    "extract",
    "projectcontext",
    "techstack",
    "codebase-structure",
    "coding-standards",
    "rules",
    "story",
    "refine",
    "clarify",
    "changerequest",
    "finalize",
    "tasks",
    "implement",
    "review",
    "diagram",
    "quickfix",
)


def lifecycle_commands() -> tuple[Command, ...]:
    remaining = {command.name: command for command in COMMANDS}
    ordered = [remaining.pop(name) for name in LIFECYCLE_ORDER if name in remaining]
    # A new contract that is not yet placed in the route still has to reach every listing.
    ordered.extend(remaining[name] for name in sorted(remaining))
    return tuple(ordered)
