"""Write markdown for the README."""

import yaml
from collections import defaultdict

DATA_PATH = 'data.yaml'
TITLE = 'AoC developer resources'
DESCRIPTION = 'Useful repositories and articles related to developing software and analysis for Age of Empires II.'


def append(text, line):
    """Append a line to the text."""
    return text + '{}{}'.format(line, '\n')


def write_markdown(data):
    """Write markdown based on data file."""
    text = ''
    text = append(text, "# {}".format(TITLE))
    text = append(text, DESCRIPTION)

    categories = defaultdict(list)
    for repo in data['repositories']:
        categories[repo['category']].append(repo)

    text = append(text, "## Repositories")
    for cat, repos in categories.items():
        text = append(text, '### {}'.format(cat))
        text = append(text, "| Repository | Language | Maturity | Version |")
        text = append(text, "| --- | --- | --- | --- |")
        for repo in repos:
            text = append(text, '| [{}]({}) | {} | {} | {} |'.format(
                repo['name'], repo['url'], repo['language'], repo['maturity'], repo['version'])
            )

    text = append(text, "## Articles")
    for article in data['articles']:
        text = append(text, '- [{}]({})'.format(article['name'], article['url']))

    return text


if __name__ == '__main__':
    """Script entry point."""
    with open(DATA_PATH) as handle:
        print(write_markdown(yaml.safe_load(handle)))
