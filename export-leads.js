// Simple script to export leads from localStorage
// Run in browser console on the leads page
const leads = JSON.parse(localStorage.getItem('leads') || '[]');
console.log(JSON.stringify(leads, null, 2));
