# Migrating to Git Source Code Hosting

Design Doc

# The Problem

In a blog post dated August 20, 2019\[1\], Bitbucket announced that it
would be disabling the creation of new mercurial repositories on the
site starting February 1, 2020, freezing all mercurial functionality
starting on June 1, 2020, and eventually deleting all mercurial
repositories from the site. Out of our many shared and personal
repositories on bitbucket, few, if any, use git.

# The Plan

All repositories owned by the [<span class="underline">natcap bitbucket
team</span>](http://bitbucket.org/natcap) will be migrated to
GitHub\[2\] and stored under our [<span class="underline">github
organization</span>](http://github.com/natcap). We also have teams on
bitbucket and gitlab for those natcappers who would prefer those
platforms (email James for access), but the software team’s active
development will be on github.

## Tracking the Progress of Migration

Migration progress will be tracked under the github repository
[<span class="underline">natcap/mercurial-migration-plan</span>](https://github.com/natcap/mercurial-migration-plan).
The specifics of what is in progress by the software team can be viewed
in the issue queue, or in the [<span class="underline">Mercurial
Migration project</span>](https://github.com/orgs/natcap/projects/2)
owned by the natcap organization.

## What to do about Bitbucket

Once repositories have been migrated from bitbucket to github and the
repository has been annotated with the URL to the repo’s new home, we’ll
just leave it there. If bitbucket wants to delete the repo later on,
that’s fine. We’ll be long gone.

## Process for Repository Migration

Each repository is a bit different and may need special consideration
during migration to accommodate the development processes and repository
structure of the individual project. The decision-makers for a given
repo’s migration will be determined, with the project maintainer (for
projects with a clear deliverable) or active contributors (in the case
of a collaborative experiment) being possibilities.

The migration of a repository from BitBucket to GitHub consists of:

1.  > **Close open issues and PRs.** Take a look at the issues and PRs
    > open on the bitbucket project. Can they be closed before
    > migration? If so, consider completing them before migration.

2.  > **Convert the repo to git.** Convert the source tree from
    > mercurial to git and pushing the converted source tree to its new
    > repository.
    
    1.  > If the repository being migrated has no meaningful branching,
        > consider using the [<span class="underline">github repository
        > importer</span>](https://github.com/new/import). This will
        > create the new repository for you.
    
    2.  > If branch names matter, use
        > [<span class="underline">hg-fast-export</span>](https://github.com/frej/fast-export)
        > with the “branch\_name\_in\_commit” plugin to prepend or
        > append branch names to commit messages during repository
        > conversion. This will require manual creation of the new
        > repository.
    
    3.  > Repositories that are to be maintained but non-active should
        > be *Archived* through the repo’s settings, rendering their
        > issue queues and source trees completely read-only.

3.  > **Set up [<span class="underline">branch restrictions for the
    > repository</span>](https://help.github.com/en/articles/enabling-branch-restrictions)**
    > if needed. These will be required for core software projects like
    > InVEST, Pygeoprocessing, taskgraph and ecoshard. By default, a
    > repository should not have any branch permissions restrictions.

4.  > **Migrate issues for the repository (if desired)**
    
    4.  > To migrate all issues programmatically, use
        > [<span class="underline">https://github.com/jeffwidman/bitbucket-issue-migration</span>](https://github.com/jeffwidman/bitbucket-issue-migration).
        > Otherwise, if only copying over specific issues, these can be
        > created manually.
    
    5.  > If not migrating issues:
        
        1.  > Be sure to use the \`hg-fast-export\` repo conversion
            > method and modify the plugins to re-write issue numbers
            > with a relevant prefix. This will work around
            > github/bitbucket issue number collisions within commit
            > messages.
        
        2.  > Be sure to export the contents of the issue tracker and
            > back them up to cold storage.

5.  > **Migrate any wiki pages** to an appropriate home on github such
    > as API documentation or a wiki associated with the target
    > repository.

6.  > **Set up new CI services** in the new repository
    
    6.  > GitHub Actions looks promising for automating repository
        > workflows (e.g. automated branching and tagging on a PR),
        > though it is still in beta.
        
        3.  > Note that the natcap organization has access to the beta.
            > Other users can [<span class="underline">sign up for early
            > access here</span>](https://github.com/features/actions).
    
    7.  > Third-party CI services such as
        > [<span class="underline">Travis</span>](https://docs.travis-ci.com/),
        > [<span class="underline">AppVeyor</span>](https://www.appveyor.com/docs/),
        > [<span class="underline">Azure
        > DevOps</span>](https://docs.microsoft.com/en-us/azure/devops/?view=azure-devops)
        > and others may be preferable for testing and building.

7.  > **Update internal links to the repo’s new home.** If the migrated
    > repository represents a python project, be sure to update internal
    > references to refer to its new home on github:
    
    8.  > Setup.py should refer to the new repository
    
    9.  > Ensure paths in build configuration (such as a Makefile) refer
        > to the correct places
    
    10. > Any automated documentation building (such as readthedocs.org)
        > may need to have its links updated.

8.  > **Close down the old repository** by linking to the new home on
    > github somewhere in the bitbucket project.

9.  > **Fork the repository.** If the repo uses a fork model for
    > contributions, contributors will need to re-fork the repo on
    > github.

At this point, all active development for the migrated repository should
be taking place exclusively on github.

### Priority Repositories for Migration

1.  > Core, actively-developed software repositories
    
    1.  > Taskgraph
    
    2.  > Pygeoprocessing
    
    3.  > InVEST and its User’s Guide (test/sample data repos need not
        > be migrated as of yet as they are already git repositories)
    
    4.  > Ecoshard

2.  > Repositories that represent software applications with defined
    > distributions not maintained by the Software Team (e.g. MESH,
    > Rangelands)

3.  > Repositories that represent source-controlled, CNAME’d buckets on
    > GCP, such as the museum, msp and tradeoffgames repos.

4.  > InVEST Sample and Test data repositories (will require updates to
    > billing due to repository sizes and expected bandwidth)

5.  > All other repositories
    
    5.  > Repositories without commits or with trivial contents will not
        > be migrated.
    
    6.  > All others will be handled appropriately for whatever they
        > are.

Github does not currently have a way to group repositories within an
organization outside of project boards (which don’t have an obvious way
to link repositories).

### Special Cases

  - > OPAL’s migration plan is documented separately.

  - > RIOS will be migrated but will be marked as *Archived* on github.

  - > Invest-natcap.invest-3 will be migrated but marked as *Archived*.

  - > All repositories under the
    > [<span class="underline">Natcap-Archive</span>](https://bitbucket.org/natcap-archive/?visibility=all)
    > project will be backed up to NatCap’s Cold Storage and will not be
    > migrated to github.

## Process for Snippet Migration

**NOTE: the process outlined below \*should\* work, in theory. In
practice, I have not yet been able to get this to work.**

Bitbucket snippets and github gists are interesting in that while they
are hg/git repositories, they always have a single commit in them at the
time of creation. This makes it tricky to

Bitbucket snippets should be converted to github gists or git snippets
on a different source code hosting platform. The process for this is:

1.  > Convert the snippet’s repository from mercurial to git.

2.  > Create a new gist/snippet on the target account, probably with the
    > same name as the one you are migrating

3.  > Once you have the new git repository, add the gist ssh remote URI
    > to your snippet git repo and push to the new origin.
    
    1.  > NOTE: this \*should\*, in theory, work if you \`git push
        > \<gist origin\> --all --force-with-lease\` to the new origin.
        > I have not been able to get this to work in practice.

#   

# Appendix: Notes

Why we were on bitbucket: mercurial support, and it \*was\* a huge step
up from google code at the time.

Link to old design document about bitbucket migration?

Why we were using mercurial at all

Historical reasons:

  - > All existing repos were already in mercurial

  - > Mercurial was a sensible choice for our use case (comms team used
    > hg for website, science staff used hg for UG repo, a few others
    > used hg for things)

  - > When we started using source control, git was around but was
    > tricky to get working on Windows (since then, git support on
    > Windows has dramatically improved)

  - > The UI for hg was far superior to git. Still is. Since we started
    > hosting our source code, many GUI applications for git have made
    > interacting with git a lot easier, and the advent of hg-git even
    > allows for hg to be a useful interface for git repos.

Is it worth staying with mercurial?

It once was, yes, but probably isn’t any longer:

  - > Hg-git (supposedly) can still be used as an hg interface for git

  - > It’s rare to find CI solutions that offer out-of-the-box support
    > for mercurial, but every service I’ve tried to use in the last few
    > years supports git. Migrating to git would make my life building
    > and distributing binaries much easier.

  - > Admittedly, git’s branching scheme is convenient as we can safely
    > delete branches (akin to hg bookmarks) without messing up history.

  - > Git support on windows is basically where it has needed to have
    > been

Is bitbucket sufficient for our needs?

  - > Pipelines/appveyor made it possible for us to abandon most jenkins
    > functionality (which was great). We are starting to have a need
    > for greater automation, which I would prefer to automate within
    > the same source control repository.

  - > Pipelines (and appveyor, for that matter) never had support for
    > mac builds

  - > Bitbucket’s issue tracker is workable, though limited. Clearly
    > Atlassian is trying to get us to use JIRA for more advanced issue
    > tracking.

  - > We need reliable source control hosting. Bitbucket has been this
    > for us.

  - > Repositories need to be able to have associated issue tracking.
    > Bitbucket has this for us.

  - > I have been missing an effective way to plan releases within the
    > issue tracker. Github has a superior dashboard for this, as does
    > JIRA.

  - > Github is, decidedly, the de facto home of open-source.

There isn’t just the question of whether bitbucket is sufficient, but
whether there is something that would make our lives easier.

Reasons to stay with bitbucket

  - > Assuming there is an easy way to convert mercurial repositories to
    > git behind the scenes, we could continue about our daily lives.
    
      - > Repos with pipelines would be able to continue operating
        > without issue.
    
      - > No additional work would be required to continue using the
        > same interfaces we’ve been using for some time now.

Reasons to migrate to github specifically

  - > De facto home of open-source software. Migrating here would,
    > admittedly, make our work more visible (for better or for worse).

  - > Version/release planning and related release management is a
    > better experience on github

  - > There are some excellent github-only integrations (including CI
    > services such as travis) that really could help us improve the
    > quality of our work with minimal work on our part to set up and
    > maintain the integrations.

  - > Github’s in-house CI appears to be intended to manage repository
    > actions in addition to the usual build and distribution processes.
    > This could be very useful to us for the sort of automation we’re
    > hoping to add (e.g. automated releases)

  - > Github’s kanban boards integrate nicely with PR processes (should
    > we decide to use kanban boards), and these boards can even belong
    > to the whole team across repositories. It’s the sort of
    > overarching project management that makes way more sense to me
    > than JIRA did, and since almost everything we do as a software
    > team is attached to our repositories, it makes sense to use this
    > feature here as well.
    
      - > Plus, it’s arguable that our science should be open as well,
        > so we can orchestrate and plan work here, out in the open.

Proposed migration process:

  - > Migrate taskgraph to natcap team on github
    
      - > *Objective: try out the migration on one of our simplest
        > repositories. Main thing would be to properly complete the
        > migration and get issues to update as expected.*
    
      - > ~~Migrate issues (write new migration script)~~
    
      - > Migrate source tree (use github importer)
    
      - > Automate cross-OS testing
    
      - > Automate package building and distribution to PyPI

  - > Migrate pygeoprocessing to natcap team on github
    
      - > Objective: try to migrate a project with a complicated binary
        > build process.
    
      - > ~~Migrate issues (use TG migration script)~~
    
      - > Migrate source tree (use github importer)
    
      - > Automate cross-OS testing
    
      - > Automate package building with multiple OSes and distribution
        > to PyPI

  - > Migrate natcap.invest to natcap team on github
    
      - > Objective: InVEST is the most complicated repository we have.
        > If this works, we’re pretty much good to go.
    
      - > ~~Migrate issues (use TG migration script)~~
    
      - > Migrate source tree (use github importer)
    
      - > Automate cross-os testing
    
      - > Automate package building on Windows and Mac
    
      - > Automate mac/linux/windows testing
    
      - > Automate distribution to PyPI

Remaining work to do before migrating to github:

  - > Figure out a new branching scheme and how github actions might
    > play into this.

  - 
<!-- end list -->

1.  *Sunsetting Mercurial Support in Bitbucket*,
    [<span class="underline">https://bitbucket.org/blog/sunsetting-mercurial-support-in-bitbucket</span>](https://bitbucket.org/blog/sunsetting-mercurial-support-in-bitbucket)

2.  As of writing, the most popular options for hosted git repositories
    are [<span class="underline">GitHub</span>](https://github.com/),
    [<span class="underline">GitLab</span>](https://about.gitlab.com/)
    and
    [<span class="underline">BitBucket</span>](https://bitbucket.org).
    While each has their benefits, GitHub remains the *de facto* home of
    open-source software projects, has excellent integrations with
    hosted CI services that we would benefit from and has good built-in
    project and team management capabilities compared with GitLab and
    BitBucket.
