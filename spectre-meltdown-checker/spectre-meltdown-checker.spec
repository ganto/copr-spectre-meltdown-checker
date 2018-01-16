Name:       spectre-meltdown-checker
Version:    0.31
Release:    0.2%{?dist}

Summary:    Spectre & Meltdown vulnerability/mitigation checker for Linux
License:    GPLv3
URL:        https://github.com/speed47/spectre-meltdown-checker
Source0:    https://github.com/speed47/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   gawk
Requires:   bash
Requires:   binutils
Requires:   coreutils
Requires:   gzip
Requires:   grep
Requires:   sed
Requires:   which
%if 0%{?rhel} == 6
Requires:   module-init-tools
Requires:   util-linux-ng
%else
Requires:   kmod
Requires:   util-linux
%endif

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
* Tue Jan 16 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.31-0.2
- Fix dependency definitions

* Tue Jan 16 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.31-0.1
- Initial package


