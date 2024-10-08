# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate ndarray-rand

Name:           rust-ndarray-rand
Version:        0.15.0
Release:        %autorelease
Summary:        Constructors for randomized arrays. rand integration for ndarray

License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ndarray-rand
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Constructors for randomized arrays. `rand` integration for `ndarray`.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/LICENSE-APACHE
%license %{crate_instdir}/LICENSE-MIT
%doc %{crate_instdir}/README.md
%doc %{crate_instdir}/RELEASES.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+quickcheck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+quickcheck-devel %{_description}

This package contains library source intended for building other packages which
use the "quickcheck" feature of the "%{crate}" crate.

%files       -n %{name}+quickcheck-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
%cargo_test -a
%endif

%changelog
%autochangelog
