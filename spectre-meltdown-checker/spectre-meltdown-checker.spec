Name:       spectre-meltdown-checker
Version:    0.32
Release:    0.1%{?dist}

Summary:    Spectre & Meltdown vulnerability/mitigation checker for Linux
License:    GPLv3
URL:        https://github.com/speed47/spectre-meltdown-checker
Source0:    https://github.com/speed47/%{name}/archive/v%{version}.tar.gz#/%{name}-%{version}.tar.gz

BuildArch:  noarch

Requires:   /bin/sh
Requires:   binutils
Requires:   coreutils
Requires:   gawk
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

BuildRequires: help2man

%description
%{summary}.

%prep
%autosetup -n %{name}-%{version}

%build

%install
install -D --preserve-timestamps %{name}.sh %{buildroot}%{_bindir}/%{name}
install -d %{buildroot}%{_mandir}/man1
help2man %{buildroot}%{_bindir}/%{name} -n "Spectre and Meltdown mitigation detection tool" \
    --no-info --version-string=%{version} --output=%{buildroot}%{_mandir}/man1/spectre-meltdown-checker.1

%files
%doc README.md
%license LICENSE
%{_bindir}/*
%{_mandir}/*

%changelog
* Tue Jan 16 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.31-0.2
- Fix dependency definitions

* Tue Jan 16 2018 Reto Gantenbein <reto.gantenbein@linuxmonk.ch> 0.31-0.1
- Initial package


