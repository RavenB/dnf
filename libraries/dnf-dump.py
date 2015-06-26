#
# Author:: AJ Christensen (<aj@junglistheavy.industries>)
# Author:: Joe Miller (<joeym@joeym.net>)
# Copyright:: Copyright (c) 2015 Pantheon Systems, Ltd
# License:: Apache License, Version 2.0
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import dnf
import dnf.sack
import dnf.cli
# from dnfpluginsextra import _

# TODO(fujin): may not make sense to have this as a dnf plugin - we just need to use the sack.
class DnfDump(dnf.Plugin):
    name = 'dnf-dump'

    def __init__(self, base, cli):
        super(DnfDump, self).__init__(base, cli)
        if cli:
            cli.register_command(DnfDumpCommand)