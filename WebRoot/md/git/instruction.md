# 常见指令

### 基本操作

> git init    

初始化仓库，即将一个文件夹定义为 git 仓库。初始化之后，文件夹中多处一个 .git 的隐藏文件夹，用于存储版本信息。删除这个文件夹，这个 git 仓库又就变成了文件夹。

> git status

显示当前 git 仓库的状态。

> git add

向暂存区添加文件，可以是单个文件，也可以用 `git add .` 代替，表示添加所有文件。

> git commit

提交暂存区中的内容到仓库，可以在后面加 `-m` 用于追述提交信息。

> git log

查看仓库提交日志。

- `--pretty=short` 只显示提交信息的第一行。
- `[目录/文件名]` 只显示指定目录或文件的日志信息。
- `-p` 显示文件提交所带来的改动。
- `-n` 只显示前 n 次提交。
- `--graph` 图形显示提交信息。

> git diff

查看工作树与暂存区的差别。`git diff HEAD` 查看工作树和最新提交的差别。建议在每次 `git commit` 之前，用`git diff HEAD`查看一下本次提交与上次提交的差别。

### 分支操作

> git branch 

显示所有分支

> git checkout -b [name]

创建一个分支，并切换至该分支。

> git merge [分支名]

合并分支，首先需要切换到要合并到的分支，然后执行该语句。    
如，将featureA合并到master，需要先`git checkout master`，然后执行`git merge featureA`。    
为了在历史记录中明确记录下本次合并，我们需要创建合并提交，往往需要加上`--no-ff`，因此，上面的合并指令就变为了`git merge --no-ff featureA`。

### 更改提交的操作

> git reset

回溯历史版本，`git reset --hard [版本哈希值]`来回溯到指定版本。（可以利用`git log`去查看版本哈希值，实际操作中不一定要输入完全，哈希值只需输入一部分即可）。

### 关联远程仓库

> git remote add

添加远程仓库。    
例如：`git remote add origin git@github.com:BaoXuebin/HelloWorld.git` 就是将本地仓库关联到远程仓库，并默认`origin`为远程仓库的名称。


> git push 

推送至远程仓库。

- `-u` 可以在推送的同时，将远处库指定的分支设置为本地仓库当前分支的upstream（上游）。等到使用 `git pull`从远程仓库拉取的时候，就不用再输入多余的参数。

例如： `git push -u origin master`是将本地仓库的当前分支推送到远程仓库的 master 分支上。

> git clone

在本地获取远程仓库，并且默认和远程仓库进行了关联。

> git pull

获取最新的远程仓库分支。


