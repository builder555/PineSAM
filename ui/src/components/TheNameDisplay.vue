<script setup>
import { ref } from 'vue';
defineProps(['name', 'version']);
defineEmits(['reload']);
const isNameHidden = ref(true);
</script>
<template>
  <h1 class="title">
    <a class="restore-click" @click="isNameHidden = !isNameHidden || !name">
      <span v-if="isNameHidden">PineSAM</span>
      <span v-else>{{ name }}</span>
    </a>
    <span class="tag" v-show="version"> v{{ version }} </span>
    <a class="icon refresh-button restore-click" @click="$emit('reload')">
      <i class="fas fa-sync-alt"></i>
    </a>
  </h1>
</template>
<style scoped>
.refresh-button {
  font-size: 1.2rem;
  margin: 0 0 0 0.5rem;
}
</style>
