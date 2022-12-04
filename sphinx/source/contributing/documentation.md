## 📁 `git` submodules

1. pull latest changes to submodules that have been updated by `dependabot`:

```
git pull --recurse-submodules
```

or, to make this the default `pull` behaviour:

```
git config --global submodule.recurse true
```

`dependabot` is [set up to track changes in the submodule parent repositories](https://docs.github.com/en/code-security/dependabot/dependabot-version-updates/configuration-options-for-the-dependabot.yml-file#registries):

```
.github/dependabot.yml
```

`dependabot` pull requests are [approved](https://docs.github.com/en/code-security/dependabot/working-with-dependabot/automating-dependabot-with-github-actions#approve-a-pull-request) and [merged](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request) automatically through GitHub actions.

[Automatically merging a pull request](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/incorporating-changes-from-a-pull-request/automatically-merging-a-pull-request):

```
.github/workflows/dependabot_auto_approve.yml
.github/workflows/dependabot_auto_merge.yml
```

📚 [Getting started with GitHub actions](https://docs.github.com/en/actions/quickstart)