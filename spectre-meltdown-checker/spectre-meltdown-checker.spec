Name:       spectre-meltdown-checker
Version:    0.31
Release:    0.1%{?dist}

Summary:    Spectre & Meltdown vulnerability/mitigation checker for Linux
License:    GPLv3
URL:        https://github.com/speed47/spectre-meltdown-checker
Source0:    https://github.com/speed47/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   awk
Requires:   bash
Requires:   binutils
Requires:   coreutils
Requires:   gzip
Requires:   grep
Requires:   kmod
Requires:   sed
Requires:   util-linux
Requires:   which

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build

%install
install -D --preserve-timestamps %{name}.sh %{buildroot}%{_bindir}/%{name}

%files
%doc README.md
%license LICENSE
%{_bindir}/*

%changelog
* Tue Jan 16 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.31-0.1
- Initial package


