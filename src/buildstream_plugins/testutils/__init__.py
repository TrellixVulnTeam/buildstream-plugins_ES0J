from buildstream._testing import register_repo_kind

from .repo import Bzr, Git


# TODO: can we get this from somewhere? pkg_resources?
package_name = "buildstream_plugins"


def register_sources():
    register_repo_kind("bzr", Bzr, package_name)
    register_repo_kind("git", Git, package_name)
