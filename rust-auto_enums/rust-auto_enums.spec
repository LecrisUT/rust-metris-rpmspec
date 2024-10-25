# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate auto_enums

Name:           rust-auto_enums
Version:        0.8.6
Release:        %autorelease
Summary:        Library for to allow multiple return types by automatically generated enum

License:        Apache-2.0 OR MIT
URL:            https://crates.io/crates/auto_enums
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
# * - remove older futures and tokio dependencies
Patch:          auto_enums-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24
BuildRequires:  tomcli

%global _description %{expand:
A library for to allow multiple return types by automatically generated
enum.}

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
%doc %{crate_instdir}/CHANGELOG.md
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

%package     -n %{name}+convert-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+convert-devel %{_description}

This package contains library source intended for building other packages which
use the "convert" feature of the "%{crate}" crate.

%files       -n %{name}+convert-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+coroutine_trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+coroutine_trait-devel %{_description}

This package contains library source intended for building other packages which
use the "coroutine_trait" feature of the "%{crate}" crate.

%files       -n %{name}+coroutine_trait-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fmt-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fmt-devel %{_description}

This package contains library source intended for building other packages which
use the "fmt" feature of the "%{crate}" crate.

%files       -n %{name}+fmt-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+fn_traits-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+fn_traits-devel %{_description}

This package contains library source intended for building other packages which
use the "fn_traits" feature of the "%{crate}" crate.

%files       -n %{name}+fn_traits-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures03-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures03-devel %{_description}

This package contains library source intended for building other packages which
use the "futures03" feature of the "%{crate}" crate.

%files       -n %{name}+futures03-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+generator_trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+generator_trait-devel %{_description}

This package contains library source intended for building other packages which
use the "generator_trait" feature of the "%{crate}" crate.

%files       -n %{name}+generator_trait-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+http_body1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+http_body1-devel %{_description}

This package contains library source intended for building other packages which
use the "http_body1" feature of the "%{crate}" crate.

%files       -n %{name}+http_body1-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ops-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ops-devel %{_description}

This package contains library source intended for building other packages which
use the "ops" feature of the "%{crate}" crate.

%files       -n %{name}+ops-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rayon-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rayon-devel %{_description}

This package contains library source intended for building other packages which
use the "rayon" feature of the "%{crate}" crate.

%files       -n %{name}+rayon-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+std-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+std-devel %{_description}

This package contains library source intended for building other packages which
use the "std" feature of the "%{crate}" crate.

%files       -n %{name}+std-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio1-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio1-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio1" feature of the "%{crate}" crate.

%files       -n %{name}+tokio1-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+transpose_methods-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+transpose_methods-devel %{_description}

This package contains library source intended for building other packages which
use the "transpose_methods" feature of the "%{crate}" crate.

%files       -n %{name}+transpose_methods-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+trusted_len-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+trusted_len-devel %{_description}

This package contains library source intended for building other packages which
use the "trusted_len" feature of the "%{crate}" crate.

%files       -n %{name}+trusted_len-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+type_analysis-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+type_analysis-devel %{_description}

This package contains library source intended for building other packages which
use the "type_analysis" feature of the "%{crate}" crate.

%files       -n %{name}+type_analysis-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+unstable-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+unstable-devel %{_description}

This package contains library source intended for building other packages which
use the "unstable" feature of the "%{crate}" crate.

%files       -n %{name}+unstable-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep
# Cannot compile tests yet because they are using multiple forked projects
# Tracker is of a similar issue by the same author
# https://github.com/taiki-e/derive_utils/issues/48
tomcli set Cargo.toml arrays delitem --key path test tests/compiletest.rs
tomcli set Cargo.toml arrays delitem --key path test tests/expandtest.rs

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
