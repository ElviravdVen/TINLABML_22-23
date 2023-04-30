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

[Git (Windows)](https://gitforwindows.org/)

</li>

<li>

[Git (Mac)](https://git-scm.com/download/mac)

</li>

<li>

**Install [GitHub CLI](https://cli.github.com/) (MacOS only)**

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

otherwise copy and paste the content of your SSH <u>public</u> key to a [new ssh key in GitHub](https://github.com/settings/ssh/new)

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

Run the following commands from your TINLABML_22-23 directory with your own github username and email address:

```sh
git config user.name "github_username"
git config user.email "student@hr.nl"
```

Once done, you can confirm that the information is set by running (see the last two lines):

```sh
git config --list
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

Create virtual Python environment 

```sh
python -m venv tinlab
```

Activate virtual Python environment 

Run the following command and add it to your <i>.bashrc</i> or <i>.zshrc</i> to make it the default

in Windows

```sh
tinlab/Scripts/activate.bat
```

in MacOS

```sh
source tinlab/bin/activate
```

</li>

<li>

Install Python libraries

```bash
python -m pip install --upgrade pip --no-cache-dir -r requirements.txt
```

</li>

</ul>

</li>

<li>

Visual Studio Code (VSCode)

<ul>

<li>

**Install [Visual Studio Code](https://code.visualstudio.com)**

</li>

<li>

**Enable VSCode to be opened from the command line (macOS only)**

In VSCode, open the Command Palette and type 'shell command' in order to select the Shell command: 
Install 'code' command in PATH

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

**Install VSCode Extensions**

<ul>

<li>

[Python extension](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

</li>

<li>

[Black formatter](https://marketplace.visualstudio.com/items?itemName=ms-python.black-formatter)

</li>

<li>

[Git Easy extension](https://marketplace.visualstudio.com/items?itemName=bibhasdn.git-easy)

</li>

<li>

[Markdown All in One](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)

</li>

<li>

[Jupyter](https://marketplace.visualstudio.com/items?itemName=ms-toolsai.jupyter)

</li>

<li>

[Mermaid extension](https://marketplace.visualstudio.com/items?itemName=bierner.markdown-mermaid)

</li>

<li>

[Graphviz (dot) language support](https://marketplace.visualstudio.com/items?itemName=joaompinto.vscode-graphviz)

</li>

</ul>

</li>

</ul>

</li>

<li>

VirtualBox

<ul>

<li>

Install [VirtualBox](https://www.virtualbox.org/)

</li>

<li>

Install [VirtualBox 7.0.8 Oracle VM VirtualBox Extension Pack](https://www.virtualbox.org/wiki/Downloads?ref=vnxi.net)

</li>

<li>

Install [Vagrant](https://www.vagrantup.com/)

</li>

</ul>

</li>

</ol>

## Torcs

<p>A preinstalled Torcs Environment is available as a [VirtualBox provisioned by Vagrant](https://app.vagrantup.com/AlxcNL/boxes/torcs-server/versions/0.2)</p>

<ol>

<li>

**Spin up a Virtual Ubuntu Desktop Environment**

<p>In <i>opdrachten/groepsopdracht_final_torcs</i> run 

```sh
./start_vbox.sh
```
</p>

</li>

<li>

**Login**

<p>

Enter the Ubuntu Virtual Machine (VM) and login with password <i>vagrant</i><br>
To <strong>escape</strong> from the VM press 
<ul>

<li>Right Control Key (Windows)</li>

<li>Left Control Key (MacOS)</li>

</ul>

</p>

</li>

<li>

**Start Torcs Server**

<p>Open a terminal and enter

```sh
/vagrant/start_server.sh
```

In the Torcs GUI select 
<i>Race</i> -> <i>Quick Race</i> -> <i>New Race</i>

</p>

</li>

**Test with Torcs Client**

<p>Open a second terminal(tab) and enter

```sh
/vagrant/start_client.sh
```

you will now see an autonomous racing car in the Torcs GUI.

</li>

</ol>

</li>

</ul>
