<script setup>
import { ref } from 'vue';
defineProps(['name', 'isNewAvailable']);
const isNameHidden = ref(true);
</script>
<template>
  <div v-if="isNewAvailable" class="new-available restore-click"><a href="https://github.com/builder555/PineSAM/releases/latest" target="_blank">New Version Available</a></div>
  <h1 class="title">
    <a class="restore-click" @click="isNameHidden = !isNameHidden || !name">
      <span class="accent" v-if="isNameHidden">PineSAM</span>
      <span class="accent small" v-else>{{ name }}</span>
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
.small {
  font-size: 0.8em;
}
.new-available {
  position:absolute;
  font-size: 0.7rem;
  font-family: inherit;
  top:3rem;
  z-index:1;
}
</style>
