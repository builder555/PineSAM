<script setup>
import { useAppStore } from '../stores/appstore';
import { ref, watch, nextTick } from 'vue';
const props = defineProps(['setting', 'name']);
const isRawValueVisible = ref(false);
const rawInput = ref(null);
const store = useAppStore();
const localValue = ref(store.settings[props.name].value);
watch(isRawValueVisible, (isVisible) => {
  if (isVisible) {
    nextTick(() => {
      rawInput.value.focus();
    });
  }
});
watch(localValue, (value) => {
  store.settings[props.name].value = value;
});
const updateSetting = (name, value) => {
  store.updateSetting(name, value);
  isRawValueVisible.value = false;
};
watch(
  () => store.settings[props.name].value,
  (value) => {
    if (value === localValue.value) return;
    setTimeout(() => {
      // range sliders get stuck if min+max+value are changed quickly,
      localValue.value = value;
    }, 0);
  },
);
</script>
<template>
  <div class="is-flex is-flex-grow-1">
    <input
      type="range"
      class="mr-1 is-flex-grow-1"
      :min="setting.component.min"
      :max="setting.component.max"
      :step="setting.component.step"
      @mouseup="updateSetting(name, setting.value)"
      @touchend="updateSetting(name, setting.value)"
      @blur="updateSetting(name, setting.value)"
      v-model="localValue"
    />
    <div v-show="isRawValueVisible" class="field tag px-0 m-0">
      <input
        class="input px-1 mx-0 is-info py-0"
        type="number"
        style="height: 2em"
        maxlength="3"
        ref="rawInput"
        pattern="[0-9]*"
        @keyup.enter.prevent.stop="updateSetting(name, setting.value)"
        @blur="updateSetting(name, setting.value)"
        v-model="localValue"
      />
    </div>
    <div v-show="!isRawValueVisible" class="tag is-info" @click="() => (isRawValueVisible = !isRawValueVisible)">
      {{ (setting.component.display && setting.component.display(setting.value)) || setting.value }}
    </div>
  </div>
</template>
