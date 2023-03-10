<script setup>
import { useAppStore } from '../stores/appstore';
defineProps(['setting', 'name']);
const store = useAppStore();
const cbName = 'cb-' + Math.random().toString(36);
</script>
<template>
  <div class="checkbox">
    <input
      :checked="setting.value"
      :id="cbName"
      type="checkbox"
      @change="store.updateSetting(name, $event.target.checked)"
    />
    <label :for="cbName"></label>
  </div>
</template>
