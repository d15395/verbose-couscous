# verbose-couscous
This creates a base python package template for beginners to get started with
1. Dependency management 
2. Running build-time and setup scripts in python


To use this in your project, you can clone the repository, and rename the remote respository,
using the commands
1. `git remote rm origin` to remove reference to `verbose-couscous` as the project's remote repository
2. `git remote add origin <new-repo-url>` to track a different remote repository of your choice.

For more details, visit:
1. [StackOverflow answer](https://stackoverflow.com/questions/7306603/whats-the-best-way-to-clone-duplicate-a-project-into-a-new-with-git)
2. [Git documentation on repo related commands](https://docs.github.com/en/github/using-git/adding-a-remote)

Alternatively, yoy can mirror the repository, as mentioned in [Git duplicate repo documentation](https://docs.github.com/en/github/creating-cloning-and-archiving-repositories/duplicating-a-repository)

Once this is done, please create the package directory under the `src/` path, and update the `[metadata]` parameters in `setup.cfg` file.