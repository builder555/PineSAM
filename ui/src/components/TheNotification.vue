<script setup>
defineProps({
  modelValue: {
    type: String,
    default: '',
  },
});
</script>
<template>
  <div class="notification is-danger" v-show="!!modelValue">
    <button class="delete" @click="$emit('update:modelValue', '')"></button>
    {{ modelValue }}
  </div>
</template>
<style scoped>
.notification {
  opacity: 1;
  animation: fade 0.5s ease-in-out;
  position: fixed;
  min-width: 15rem;
  left: 2rem;
  top: 1rem;
  z-index: 5;
}

@keyframes fade {
  0% {
    opacity: 0;
  }
  100% {
    opacity: 1;
  }
}
</style>
