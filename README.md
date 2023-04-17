# TINLABML_22-23
Practicum lesmateriaal TinLab ML cohort 2022-2023

## Workspace Setup

<ol>

<li>

Git

<ul>

<li>

**Install Git**

Make sure you select "Checkout as-is, commit Unix-style line endings" during the installation process.

<ul>

<li>

[Git for Windows](https://gitforwindows.org/)

</li>

<li>

[Git for Mac](https://git-scm.com/download/mac)

</li>

<li>

**Install [GitHub CLI](https://cli.github.com/) (MacOS)**

```bash
brew install gh
```

***NOTE***<br>
Although you could download and install GitHub CLI for Windows, I don't recommend it since it does not properly work in Git Bash.

</li>

</ul>

<li>

**Setup authentication**

<ul>

<li>

Create a ssh key-pair token

Start a (git) bash shell *and generate a secret key pair with your (own) student email adress

```sh
ssh-keygen -t Ed25519 -C student@hr.nl
```

</li>

<li>

**Transfer your <b>public</b> key to Github**

If you installed the GitHub client, you can authenticate with the following command in the terminal and select ssh for authentication

```sh
gh auth login
```

otherwise enter the following in (git) bash shell to view the contents of your public key

```sh
cat ~/.ssh/id_ed25519.pub
```
and paste this in the text area when adding a [new ssh key in GitHub](https://github.com/settings/ssh/new)

</li>

</ul>

<li>

**Create Repository**

<ul>

<li>

**Create your own repository TINLABML_22-23 on Github**

<p>
Browse to <a>github.com</a> and create <u>private</u> repository TINLABML_22-23.
</p>

</li>

<li>

**Invite the teachers to your repository**

</li>

<li>

**Clone your git repository**

<p>
Clone your git repository TINLABML_22-23 from Github to your local workspace</u>
</p>

</li>

<li>

**Download and copy subfolders of this repository**

<p>
Download this repository as zip-file and extract files and subdirectories contained in the zip-file to your (own) local git directory TINLABML_22-23.
</p>

</li>

<li>

**Configure git**

In order to commit and push your changes, you need identitify yourself.

Open a (git)bash, enter directory TINLABML_22-23 and run the following script with your (own) github username and student email address:

```bash
install/git_config.sh github_username student@hr.nl
```

</li>

<li>

**Add, commit and push the copied contents**

<p>

Run the following commands from your TINLABML_22-23 directory

```sh
git add .
git commit -m "Added contents for TINLABML_22-23"
git push
```

</p>

</li>

</ul>

</li>

</ul>

</li>

<li>

Python

<ul>

<li>

Install [python 3.10](https://www.python.org/downloads/release/python-3105/)

</li>

<li>

Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html)

</li>

<li>

Create virtual Python environment 

```sh
conda create -n tinlab
```

Activate virtual Python environment 

Run the following command and add it to your <i>.bashrc</i> or <i>.zshrc</i> to make it the default

```sh
conda activate tinlab
```

</li>

<li>

Install Python libraries

```bash
install/install_requirements.sh
```

</li>

</ul>

</li>

<li>

Visual Studio Code

<ul>

<li>

Install [Visual Studio Code](https://code.visualstudio.com)

</li>

<li>

**Enable VSCode to be opened from the command line (macOS only)**

In VSCode, open the Command Palette and type 'shell command' in order to select the Shell command: Install ‘code’ command in PATH

</li>

<li>

**Start vscode with command from current directory**

Start a (git) bash shell and enter directory TINLABML_22-23, from there use the command <i>code</i> to start vscode.

```sh
cd TINLABML_22-23
code .
```

</li>

<li>

Install Extensions

<ul>

<li>

Install the [Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

<li>

Install the [Git Easy extension](https://marketplace.visualstudio.com/items?itemName=bibhasdn.git-easy)

</li>

<li>

Install the [Mermaid extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

</li>

<li>

Install [Graphviz (dot) language support](https://marketplace.visualstudio.com/items?itemName=joaompinto.vscode-graphviz)

</li>

</ul>

</li>

</ul>

</li>

</ol>
