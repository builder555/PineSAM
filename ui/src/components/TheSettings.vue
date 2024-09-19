<script setup>
import { ref, watch, computed } from 'vue';
import settingGroups from '../setting-groups.js';
import SettingDropdown from './SettingDropdown.vue';
import SettingCheckbox from './SettingCheckbox.vue';
import SettingSlider from './SettingSlider.vue';
import SettingConfirm from './SettingConfirm.vue';
import { useAppStore } from '../stores/appstore';
import { getLocalStorageValue } from '../storage';

const componentsMap = {
  select: SettingDropdown,
  checkbox: SettingCheckbox,
  range: SettingSlider,
  confirm: SettingConfirm,
};
const store = useAppStore();
const settings = ref(store.settings);
const groups = ref(settingGroups);
const isHintVisible = ref(getLocalStorageValue('are-setting-hints-visible', true));
const debugData = computed(() => ({
  'Live temp': store.rawLiveData?.LiveTemp,
  'Set Temp': store.rawLiveData?.SetTemp,
  'Input voltage x10': store.rawLiveData?.Voltage,
  'Handle Temp in C x10': store.rawLiveData?.HandleTemp,
  'Power as PWM level': store.rawLiveData?.PWMLevel,
  'Power Source': store.rawLiveData?.PowerSource,
  'Tip Resistance x10': store.rawLiveData?.TipResistance,
  'Uptime (deciseconds)': store.rawLiveData?.Uptime,
  'Last Movement': store.rawLiveData?.MovementTime,
  'Max Temp': store.rawLiveData?.MaxTipTempAbility,
  'Raw Tip in μV': store.rawLiveData?.uVoltsTip,
  'Hall Sensor': store.rawLiveData?.HallSensor,
  'Operating Mode': store.rawLiveData?.OperatingMode,
  'Estimated Wattage x10': store.rawLiveData?.Watts,
}));
const isDebugVisible = ref(false);
watch(isHintVisible, (isVisible) => {
  localStorage.setItem('are-setting-hints-visible', isVisible);
});
const toggleGroup = (group) => {
  group.isVisible = !group.isVisible;
  localStorage.setItem(`setting-${group.name}-visible`, group.isVisible);
};
const availableItems = (groupItems) => {
  return groupItems.filter((name) => !!store.settings[name]);
};
for (const group of groups.value) {
  group.isVisible = getLocalStorageValue(`setting-${group.name}-visible`, true);
}
</script>

<template>
  <div class="columns restore-click">
    <div class="column is-half is-full-mobile">
      <div class="is-flex">
        <label class="label mx-3 mb-0 has-text-left">Save changes to flash</label>
        <div class="checkbox">
          <input v-model="store.isSaveToFlash" type="checkbox" id="sw-save-toflash" />
          <label for="sw-save-toflash"></label>
        </div>
      </div>
      <p v-show="isHintVisible" class="help px-3">
        If this is not checked, the settings will be reset to their previous values when you turn off the soldering
        iron.
        <strong
          >Note that flash has limited write cycles, saving changes frequently will reduce the life of your
          device.</strong
        >
      </p>
    </div>
    <div class="column is-half is-full-mobile has-text-left has-text-right-tablet">
      <label class="label mx-3 is-inline-block">Show Hints</label>
      <div class="checkbox is-inline-block" style="margin-bottom: -0.4rem">
        <input v-model="isHintVisible" type="checkbox" id="sw-show-hints" />
        <label for="sw-show-hints"></label>
      </div>
      <div class="is-hidden-desktop mr-1 is-inline">&nbsp;</div>
      <p v-show="isHintVisible" class="help px-3">
        <strong>You can find more information about each setting on the <a href="https://ralim.github.io/IronOS/Settings/" target="_blank">IronOS Page</a>.</strong>
      </p>
    </div>
  </div>
  <div v-if="Object.keys(settings).length > 0" class="columns is-multiline restore-click">
    <div v-for="group in groups" :key="group.name" class="column is-4-widescreen is-6-tablet is-12-mobile">
      <div class="card no-shadow">
        <button class="card-header navbar-link is-arrowless settings-header"  style="border: 0cap;" @click="toggleGroup(group)" :aria-expanded="group.isVisible">
        <h3 class="card-header navbar-link is-arrowless settings-header" >
          <p class="card-header-title">{{ group.name }}</p>
          <span class="icon">
            <i class="fa" :class="group.isVisible ? 'fa-angle-down' : 'fa-angle-right'"></i>
          </span>
        </h3>
        </button>
        <div v-show="group.isVisible" class="card-content">
          <form @submit.prevent="">
            <div
              v-for="name, index in availableItems(group.items)"
              :key="name"
              :class="settings[name].component?.class"
              class="mfield"
            >
              <div class="column is-half px-0">
                <label :id="'lbl_' + name" class="label">{{ settings[name].display }}</label>
                
              </div>
              <div class="column is-half is-flex is-justify-content-end px-0">
                <component
                  v-if="settings[name].component"
                  :is="componentsMap[settings[name].component.name]"
                  :setting="settings[name]"
                  :name="name"
                />
                <div v-else>
                  <input :aria-labelledby="'lbl_' + name" :value="settings[name].value" class="input py-0" type="text" style="height: auto" disabled />
                </div>
              </div>
              <p v-show="isHintVisible" class="help">{{ settings[name].hint }}</p>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
  <div v-if="Object.keys(debugData).length > 0" class="columns is-multiline restore-click">
    <div class="column is-4-widescreen is-6-tablet is-12-mobile">
      <div class="card no-shadow">
        <header class="card-header navbar-link is-arrowless settings-header" @click="isDebugVisible=!isDebugVisible">
          <p class="card-header-title">Debug Data</p>
          <span class="icon">
            <i class="fa" :class="isDebugVisible ? 'fa-angle-down' : 'fa-angle-right'"></i>
          </span>
        </header>
        <div v-show="isDebugVisible" class="card-content">
          Values taken from <a href="https://github.com/Ralim/IronOS/blob/dev/source/Core/BSP/Pinecilv2/ble_handlers.cpp" target="_blank">here</a>.
          <form @submit.prevent="">
            <div
              v-for="name in Object.keys(debugData)"
              :key="name"
              class="mfield my-0 py-0"
            >
              <div class="column is-half px-0 my-0">
                <label class="label">{{ name }}</label>
              </div>
              <div class="column is-half is-flex is-justify-content-end px-0">
                <input :value="debugData[name]" class="input py-0" type="text" style="height: auto" disabled />
              </div>
            </div>
          </form>
        </div>
      </div>
    </div>
  </div>
</template>

<style scoped>
.is-disabled {
  opacity: 0.5;
  pointer-events: none;
}

.navbar-link {
  align-items: center;
  display: flex;
}
.label {
  font-weight: 500;
  display: inline-flex !important;
  align-items: center;
  display: inline-block;
}
.card-content {
  padding: 0;
}
.mfield {
  display: flex;
  flex-wrap: wrap;
  margin: 2px 0;
  padding: 0.5rem;
  border-bottom: 1px solid #eaeaea;
}

.mfield .label {
  flex-grow: 1;
  margin-right: 0.5rem;
  display: block;
}

.mfield .input {
  flex-basis: 0;
  flex-shrink: 1;
  flex-grow: 1;
}

.mfield .help {
  flex-basis: 100%;
  margin-top: 0rem;
  margin-bottom: 0.5rem;
}
.settings-header {
  background-color: rgba(var(--secondary-color), 0.1);
}
.no-shadow {
  box-shadow: none;
}
</style>
