#
#            Copyright (C) 2015 QDevor
#
#  Licensed under the GNU General Public License, Version 3.0 (the License);
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#            http://www.gnu.org/licenses/gpl-3.0.html
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

DJCS_TOP = os.getcwd()
DJCS_CURRENT_SCRIPT_DIR = sys.path[0]
# DJCS_CURRENT_SCRIPT_DIR = sys.argv[0]
# DJCS_CURRENT_FILE_DIR = os.path.split(os.path.realpath(__file__))[0]

DJCS_DATA_DIR = DJCS_TOP + '/data'
DJCS_DATA_DIR = os.environ.get("QDKe_DJCS_DATA_DIR",DJCS_DATA_DIR)
if not os.path.exists(DJCS_DATA_DIR): os.makedirs(DJCS_DATA_DIR)

def getDataPath():
	dataPath = DJCS_DATA_DIR
	if not os.path.exists(dataPath):
		os.makedirs(dataPath)
	return dataPath
