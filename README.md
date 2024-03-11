[![Open in Dev Containers](https://img.shields.io/static/v1?label=Dev%20Containers&message=Open&color=blue&logo=visualstudiocode)](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/to/do)

# Next Generation Business Process Management (NGBPM)

Welcome to the NGBPM documentation repository! Here you will find comprehensive information about NGBPM (Next-Generation Business Process Management System), its features, benefits, and how it revolutionizes the way businesses manage their processes. 

## Table of Contents

1. [Introduction](#introduction)
2. [Why NGBPM?](#why-ngbpm)
3. [Key Features](#key-features)
4. [Leveraging Structurizr C4](#leveraging-structurizr-c4)
6. [Conclusion](#conclusion)
7. [Call to Action](#call-to-action)

---

## Introduction

In today's competitive business landscape, staying ahead requires more than just traditional process management tools. NGBPM represents the next evolution in Business Process Management Systems, integrating cutting-edge AI technologies to deliver unparalleled efficiency, adaptability, and security.

---

## Why NGBPM?

NGBPM isn't just another expense; it's a strategic investment in your business's future success. With its promise of a 10x return on investment (ROI) and a monthly investment of $1M, NGBPM offers transformative benefits that go beyond traditional BPM systems. By introducing self-optimizing processes that adapt in real-time, NGBPM ensures your operations are always at peak efficiency, helping you automate decision-making, cut down operational costs, and achieve exceptional results.

---

## Key Features

### AI-Powered Optimization

NGBPM leverages AI to intelligently adapt and optimize processes without human intervention, marking a significant advancement over traditional BPM systems.

### Adaptive Learning

The system grows with your business, continuously learning from patterns to improve processes and ensure peak efficiency.

### Unmatched Customization

Tailor-made solutions fit your unique business needs, offering flexibility and adaptability like never before.

### Next-Level Security

Rest easy knowing your data and processes are protected with the most advanced security features, setting new standards in BPM solution security.

---

## Leveraging Structurizr C4

The adoption of Structurizr C4 for defining NGBPM architecture plays a pivotal role in visualizing and understanding complex software systems. It facilitates the documentation of the system's architecture, providing clarity and insight into how NGBPM operates and interacts within various business environments.

---

## Conclusion

NGBPM, defined and visualized using Structurizr C4, represents the next leap in BPM technology. With its focus on AI-driven optimization, adaptive learning, and security, NGBPM offers businesses a competitive edge in today's dynamic market environment. The system's promise of a 10x ROI underscores its potential to transform business operations and achieve unprecedented levels of efficiency and growth.

---

## Call to Action

Ready to transform your business with NGBPM? Request a demo today and discover how NGBPM can unlock your business's full potential. Let's embark on this journey together, reshaping the future of business process management and setting new benchmarks for success.

---

Thank you for choosing NGBPM. Let's revolutionize your business processes and achieve extraordinary results together! 🚀🌟

## Using

_Python package_: to add and install this package as a dependency of your project, run `poetry add ngbpm`.

_Python CLI_: to view this app's CLI commands once it's installed, run `ngbpm --help`.

_Python application_: to serve this REST API, run `docker compose up app` and open [localhost:8000](http://localhost:8000) in your browser. Within the Dev Container, this is equivalent to running `poe api`.

## Contributing

<details>
<summary>Prerequisites</summary>

<details>
<summary>1. Set up Git to use SSH</summary>

1. [Generate an SSH key](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent#generating-a-new-ssh-key) and [add the SSH key to your GitHub account](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/adding-a-new-ssh-key-to-your-github-account).
1. Configure SSH to automatically load your SSH keys:
    ```sh
    cat << EOF >> ~/.ssh/config
    Host *
      AddKeysToAgent yes
      IgnoreUnknown UseKeychain
      UseKeychain yes
    EOF
    ```

</details>

<details>
<summary>2. Install Docker</summary>

1. [Install Docker Desktop](https://www.docker.com/get-started).
    - Enable _Use Docker Compose V2_ in Docker Desktop's preferences window.
    - _Linux only_:
        - Export your user's user id and group id so that [files created in the Dev Container are owned by your user](https://github.com/moby/moby/issues/3206):
            ```sh
            cat << EOF >> ~/.bashrc
            export UID=$(id --user)
            export GID=$(id --group)
            EOF
            ```

</details>

<details>
<summary>3. Install VS Code or PyCharm</summary>

1. [Install VS Code](https://code.visualstudio.com/) and [VS Code's Dev Containers extension](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-containers). Alternatively, install [PyCharm](https://www.jetbrains.com/pycharm/download/).
2. _Optional:_ install a [Nerd Font](https://www.nerdfonts.com/font-downloads) such as [FiraCode Nerd Font](https://github.com/ryanoasis/nerd-fonts/tree/master/patched-fonts/FiraCode) and [configure VS Code](https://github.com/tonsky/FiraCode/wiki/VS-Code-Instructions) or [configure PyCharm](https://github.com/tonsky/FiraCode/wiki/Intellij-products-instructions) to use it.

</details>

</details>

<details open>
<summary>Development environments</summary>

The following development environments are supported:

1. ⭐️ _GitHub Codespaces_: click on _Code_ and select _Create codespace_ to start a Dev Container with [GitHub Codespaces](https://github.com/features/codespaces).
1. ⭐️ _Dev Container (with container volume)_: click on [Open in Dev Containers](https://vscode.dev/redirect?url=vscode://ms-vscode-remote.remote-containers/cloneInVolume?url=https://github.com/to/do) to clone this repository in a container volume and create a Dev Container with VS Code.
1. _Dev Container_: clone this repository, open it with VS Code, and run <kbd>Ctrl/⌘</kbd> + <kbd>⇧</kbd> + <kbd>P</kbd> → _Dev Containers: Reopen in Container_.
1. _PyCharm_: clone this repository, open it with PyCharm, and [configure Docker Compose as a remote interpreter](https://www.jetbrains.com/help/pycharm/using-docker-compose-as-a-remote-interpreter.html#docker-compose-remote) with the `dev` service.
1. _Terminal_: clone this repository, open it with your terminal, and run `docker compose up --detach dev` to start a Dev Container in the background, and then run `docker compose exec dev zsh` to open a shell prompt in the Dev Container.

</details>

<details>
<summary>Developing</summary>

- Run `poe` from within the development environment to print a list of [Poe the Poet](https://github.com/nat-n/poethepoet) tasks available to run on this project.
- Run `poetry add {package}` from within the development environment to install a run time dependency and add it to `pyproject.toml` and `poetry.lock`. Add `--group test` or `--group dev` to install a CI or development dependency, respectively.
- Run `poetry update` from within the development environment to upgrade all dependencies to the latest versions allowed by `pyproject.toml`.

</details>
