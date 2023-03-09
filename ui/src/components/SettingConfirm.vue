<script setup>
import { useAppStore } from '../stores/appstore';
const props = defineProps(['setting', 'name']);
const store = useAppStore();
const confirm = () => {
  const yes = window.confirm(props.setting.component.message);
  if (yes) {
    store.updateSetting(props.name, props.setting.component.value);
  }
};
</script>
<template>
  <div class="is-flex is-flex-grow-1">
    <button class="button is-danger is-small is-flex-grow-1" @click.prevent="confirm">
      {{ setting.component.display }}
    </button>
  </div>
</template>
