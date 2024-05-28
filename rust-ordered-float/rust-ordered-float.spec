# Generated by rust2rpm 26
%bcond_without check
%global debug_package %{nil}

%global crate ordered-float

Name:           rust-ordered-float
Version:        4.2.0
Release:        %autorelease
Summary:        Wrappers for total ordering on floats

License:        MIT
URL:            https://crates.io/crates/ordered-float
Source:         %{crates_source}

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Wrappers for total ordering on floats.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
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

%package     -n %{name}+arbitrary-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+arbitrary-devel %{_description}

This package contains library source intended for building other packages which
use the "arbitrary" feature of the "%{crate}" crate.

%files       -n %{name}+arbitrary-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+borsh-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+borsh-devel %{_description}

This package contains library source intended for building other packages which
use the "borsh" feature of the "%{crate}" crate.

%files       -n %{name}+borsh-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+bytemuck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+bytemuck-devel %{_description}

This package contains library source intended for building other packages which
use the "bytemuck" feature of the "%{crate}" crate.

%files       -n %{name}+bytemuck-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+proptest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proptest-devel %{_description}

This package contains library source intended for building other packages which
use the "proptest" feature of the "%{crate}" crate.

%files       -n %{name}+proptest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rand-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rand-devel %{_description}

This package contains library source intended for building other packages which
use the "rand" feature of the "%{crate}" crate.

%files       -n %{name}+rand-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+randtest-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+randtest-devel %{_description}

This package contains library source intended for building other packages which
use the "randtest" feature of the "%{crate}" crate.

%files       -n %{name}+randtest-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rkyv-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rkyv-devel %{_description}

This package contains library source intended for building other packages which
use the "rkyv" feature of the "%{crate}" crate.

%files       -n %{name}+rkyv-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rkyv_16-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rkyv_16-devel %{_description}

This package contains library source intended for building other packages which
use the "rkyv_16" feature of the "%{crate}" crate.

%files       -n %{name}+rkyv_16-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rkyv_32-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rkyv_32-devel %{_description}

This package contains library source intended for building other packages which
use the "rkyv_32" feature of the "%{crate}" crate.

%files       -n %{name}+rkyv_32-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rkyv_64-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rkyv_64-devel %{_description}

This package contains library source intended for building other packages which
use the "rkyv_64" feature of the "%{crate}" crate.

%files       -n %{name}+rkyv_64-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+rkyv_ck-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+rkyv_ck-devel %{_description}

This package contains library source intended for building other packages which
use the "rkyv_ck" feature of the "%{crate}" crate.

%files       -n %{name}+rkyv_ck-devel
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

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

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