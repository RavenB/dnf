require 'spec_helper'

describe 'dnf_package_install_test::default' do

  # Serverspec examples can be found at
  # http://serverspec.org/resource_types.html

  describe package('jq') do
    it { should be_installed }
  end

  describe package('vim-enhanced') do
    it { should be_installed }
  end

  describe package('nc6') do
    it { should be_installed }
  end

end
