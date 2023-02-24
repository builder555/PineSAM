const requestWakeLock = async () => {
    let lock = undefined;
    if ('wakeLock' in navigator) {
        try {
          lock = await navigator.wakeLock.request('screen');
          lock.addEventListener('release', () => {
            console.info('Wake Lock was released');
          });
          console.info('Wake Lock is active');
        } catch (err) {
          console.error(err);
        }
    } else {
        console.info('Wakelock is not supported')
    }

    return lock;
  };    
  
const releaseWakeLock = async (lock) => {
    if (!lock) {
      return;
    }
    try {
      await lock.release();
      lock = null;
    } catch (err) {
      console.error(`${err.name}, ${err.message}`);
    }
  };

export const wakeLock = {
    request: requestWakeLock,
    release: releaseWakeLock
}