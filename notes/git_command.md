## Push local repo to Github

https://docs.github.com/en/get-started/importing-your-projects-to-github/importing-source-code-to-github/adding-locally-hosted-code-to-github

## Adding a local repository to GitHub using Git

1. [Create a new repository](https://docs.github.com/en/repositories/creating-and-managing-repositories/creating-a-new-repository) on GitHub.com. To avoid errors, do not initialize the new repository with *README*, license, or `gitignore` files. You can add these files after your project has been pushed to GitHub.![Create New Repository drop-down](https://docs.github.com/assets/cb-11427/images/help/repository/repo-create.png)

2. Open Terminal.

3. Change the current working directory to your local project.

4. Initialize the local directory as a Git repository.

   ```
   $ git init -b main
   ```

5. Add the files in your new local repository. This stages them for the first commit.

   ```shell
   $ git add .
   # Adds the files in the local repository and stages them for commit. To unstage a file, use 'git reset HEAD YOUR-FILE'.
   ```

6. Commit the files that you've staged in your local repository.

   ```shell
   $ git commit -m "First commit"
   # Commits the tracked changes and prepares them to be pushed to a remote repository. To remove this commit and modify the file, use 'git reset --soft HEAD~1' and commit and add the file again.
   ```

7. At the top of your repository on GitHub.com's Quick Setup page, click to copy the remote repository URL.![Copy remote repository URL field](https://docs.github.com/assets/cb-25662/images/help/repository/copy-remote-repository-url-quick-setup.png)

8. In Terminal, add the URL for the remote repository where your local repository will be pushed.

   ```shell
   $ git remote add origin  <REMOTE_URL> 
   # Sets the new remote
   $ git remote -v
   # Verifies the new remote URL
   ```

9. Push the changes in your local repository to GitHub.com.

   ```shell
   $ git push -u origin main
   # Pushes the changes in your local repository up to the remote repository you specified as the origin
   ```

## Add empty folders to repos

https://www.theserverside.com/blog/Coffee-Talk-Java-News-Stories-and-Opinions/gitkeep-push-empty-folders-git-commit

1. To add an empty folder, we have to use .gitkeep

   ```shell
   gitkeep@example:~$ mkdir empty-directory
   gitkeep@example:~$ cd empty-directory
   gitkeep@example:~$ touch .gitkeep
   gitkeep@example:~$ git add .
   gitkeep@example:~$ git commit -m "Commit empty folder in Git with gitkeep"
   gitkeep@example:~$ git push origin
   ```

https://www.youtube.com/watch?v=46_0Re1iEIM

## Add all to Git

```shell
(venv) (base) congwang@Congs-MacBook-Pro notes % git add -A 
```

