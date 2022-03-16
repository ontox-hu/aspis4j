{ pkgs ? import (fetchTarball https://git.io/Jf0cc) {} }:

let
  mach-nix = import (builtins.fetchGit {
    url = "https://github.com/DavHau/mach-nix";
    ref = "refs/tags/3.4.0";
  }) {};

  customPython = mach-nix.mkPython rec {
    requirements = builtins.readFile ./requirements.txt;
  };
in

pkgs.mkShell {
  buildInputs = [ customPython ];
}