class Devspec < Formula
  include Language::Python::Virtualenv

  desc "Compact, resumable spec-driven workflow templates for AI coding agents"
  homepage "https://github.com/speclabs/devspec"
  # The PyPI sdist has a stable checksum; GitHub's on-the-fly tag archives do not guarantee one.
  url "REPLACE_WITH_SDIST_URL"
  sha256 "REPLACE_WITH_RELEASE_SHA256"
  license "Apache-2.0"

  depends_on "python@3.12"

  # Build backend. Homebrew builds without isolation, and python@3.12 no longer bundles setuptools.
  resource "setuptools" do
    url "https://files.pythonhosted.org/packages/6d/44/f5da03a8ef95d369145c5bb53050e7877c9f3d312e128605fd9504829143/setuptools-84.0.0.tar.gz"
    sha256 "f4695c21257f0d9b537ec2692c941d02ee143b7cc1276941349a546573b2ef73"
  end

  def install
    virtualenv_install_with_resources
  end

  test do
    assert_match version.to_s, shell_output("#{bin}/devspec --version")
    system bin/"devspec", "init", "--target", testpath, "--profile", "all", "--repo-state", "existing"
    system bin/"devspec", "doctor", "--target", testpath, "--profile", "all"
  end
end
