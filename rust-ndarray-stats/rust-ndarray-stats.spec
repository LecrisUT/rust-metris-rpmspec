# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate ndarray-stats

Name:           rust-ndarray-stats
Version:        0.6.0
Release:        %autorelease
Summary:        Statistical routines for ArrayBase

# Upstream license specification: MIT/Apache-2.0
License:        MIT OR Apache-2.0
URL:            https://crates.io/crates/ndarray-stats
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * Relax indexmap requirement
Patch:          ndarray-stats-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli

%global _description %{expand:
Statistical routines for ArrayBase, the n-dimensional array data
structure provided by ndarray.}

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
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Do not depend on criterion; it is needed only for benchmarks.
tomcli set Cargo.toml del dev-dependencies.criterion

%generate_buildrequires
%cargo_generate_buildrequires -a

%build
%cargo_build -a

%install
%cargo_install -a

%if %{with check}
%check
# * Probably using debug_assert!
%cargo_test -a -- -- --skip entropy::tests::test_cross_entropy_with_noisy_negative_qs --skip entropy::tests::test_kl_with_noisy_negative_qs
%endif

%changelog
%autochangelog
