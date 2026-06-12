class Devspec < Formula
  include Language::Python::Virtualenv

  desc "Installer and synchronizer CLI for the devspec workflow framework"
  homepage "https://github.com/speclabs/devspec"
  url "https://github.com/speclabs/devspec/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "2df77292d932571ece075f9f17889ee622fbb8edfc9b984ceefbe1f532459ec3"
  license "Apache-2.0"

  depends_on "python@3.12"

  resource "hatchling" do
    url "https://files.pythonhosted.org/packages/63/4c/8717ccb844b4fa5a5ba6352e97d743ed24e9a22cf90b7c109c17030a46a1/hatchling-1.30.1.tar.gz"
    sha256 "eee4fd45357f72ebb3d7a42e5d72cfb5e29ed426d79e8836288926c4258d5f2e"
  end

  resource "packaging" do
    url "https://files.pythonhosted.org/packages/d7/f1/e7a6dd94a8d4a5626c03e4e99c87f241ba9e350cd9e6d75123f992427270/packaging-26.2.tar.gz"
    sha256 "ff452ff5a3e828ce110190feff1178bb1f2ea2281fa2075aadb987c2fb221661"
  end

  resource "pathspec" do
    url "https://files.pythonhosted.org/packages/5a/82/42f767fc1c1143d6fd36efb827202a2d997a375e160a71eb2888a925aac1/pathspec-1.1.1.tar.gz"
    sha256 "17db5ecd524104a120e173814c90367a96a98d07c45b2e10c2f3919fff91bf5a"
  end

  resource "pluggy" do
    url "https://files.pythonhosted.org/packages/f9/e2/3e91f31a7d2b083fe6ef3fa267035b518369d9511ffab804f839851d2779/pluggy-1.6.0.tar.gz"
    sha256 "7dcc130b76258d33b90f61b658791dede3486c3e6bfb003ee5c9bfb396dd22f3"
  end

  resource "trove-classifiers" do
    url "https://files.pythonhosted.org/packages/c2/e3/7ca82ee24c82d344584abd5b8637b3bd056f2900226e8d82fc22f1184b92/trove_classifiers-2026.6.1.19.tar.gz"
    sha256 "c5132b4b61a829d11cfbd2d72e97f20a45ed6edb95e45c5efdeb5e00836b2745"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/devspec version")
  end
end
