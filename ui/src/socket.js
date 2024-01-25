// import process from 'process';
class Socket {
  constructor() {
    this.socket = null;
    this.callbacks = new Map();
    this.callbacks.set('ERROR', this.defaultErrorHandler);
  }
  defaultErrorHandler(message) {
    console.warn(message);
  }
  initSocket() {
    // change this if you're running back-end on a different port when in development
    let port = import.meta.env.MODE === 'production' ? window.location.port : 8080; 

    return new Promise((resolve) => {
      this.socket = new WebSocket(`ws://${window.location.hostname}:${port}/`);
      this.registerCallbacks();
      this.socket.onopen = () => {
        resolve();
      };
      this.socket.onerror = (err) => {
        const cb = this.callbacks.get('ERROR');
        cb('Error connecting to backend. Make sure the server is running.');
        console.warn(err);
      };
    });
  }
  async checkSocket() {
    if (this.socket?.readyState !== WebSocket.OPEN) {
      await this.initSocket();
    }
  }
  registerCallbacks() {
    this.socket.onmessage = (message) => {
      const data = JSON.parse(message.data);
      let callback = null;
      let payload = null;
      if (data.status === 'OK') {
        callback = this.callbacks.get(data.command);
        payload = data.payload;
      } else {
        callback = this.callbacks.get('ERROR');
        payload = data.message;
        console.warn(payload);
      }
      if (callback) {
        callback(payload);
      }
    };
  }
  async send(data) {
    await this.checkSocket();
    this.socket.send(JSON.stringify(data));
  }
  on(event, callback) {
    this.callbacks.set(event, callback);
  }
}
const socket = new Socket();
export { socket };
