class Devspec < Formula
  include Language::Python::Virtualenv

  desc "Installer and synchronizer CLI for the devspec workflow framework"
  homepage "https://github.com/OWNER/devspec"
  url "https://github.com/OWNER/devspec/archive/refs/tags/v0.1.0.tar.gz"
  sha256 "REPLACE_WITH_RELEASE_SHA256"
  license "Apache-2.0"

  depends_on "python@3.12"

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/devspec version")
  end
end
