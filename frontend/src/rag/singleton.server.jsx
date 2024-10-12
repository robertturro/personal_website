export const singleton = (name, valueFactory) => {
  const g = global; // Access the global object
  g.__singletons = g.__singletons || {}; // Initialize if it doesn't exist
  g.__singletons[name] = g.__singletons[name] || valueFactory(); // Create or return the existing instance
  return g.__singletons[name]; // Return the singleton instance
};
