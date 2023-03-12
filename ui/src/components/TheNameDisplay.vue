<script setup>
import { ref } from 'vue';
defineProps(['name']);
defineEmits(['reload']);
const isNameHidden = ref(true);
</script>
<template>
  <h1 class="title">
    <a class="restore-click" @click="isNameHidden = !isNameHidden || !name">
      <span class="accent" v-if="isNameHidden">PineSAM</span>
      <span class="accent" v-else>{{ name }}</span>
    </a>
    <a class="icon primary refresh-button restore-click" @click="$emit('reload')">
      <i class="fas fa-sync-alt"></i>
    </a>
  </h1>
</template>
<style scoped>
.refresh-button {
  font-size: 1.2rem;
  margin: 0 0 0 0.5rem;
}
h1 {
  font-family: 'Righteous', "Segoe UI", Roboto, Oxygen, Ubuntu, Cantarell, "Helvetica Neue", Helvetica, Arial, sans-serif;
}
</style>
