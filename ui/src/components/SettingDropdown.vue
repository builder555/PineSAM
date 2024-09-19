<script setup>
import { ref, watch } from 'vue';
import { useAppStore } from '../stores/appstore';
const props = defineProps(['setting', 'name']);
const localValue = ref(props.setting.value);
const store = useAppStore();
watch(localValue, (value) => {
  store.updateSetting(props.name, value);
});
</script>
<template>
  <div class="is-flex-grow-1">
    <select :aria-labelledby="'lbl_' + name" v-model="localValue" class="input py-0" style="height: auto">
      <option v-for="option in setting.component.options" :key="option.value" :value="option.value">
        {{ option.text }}
      </option>
    </select>
  </div>
</template>
