import kue from "kue";

const queue = kue.createQueue();

const obj = {
  phoneNumber: '+256787304045',
  message: 'Where is my money man😐?'
};

const job = queue.create('push_notification_code', obj);

job.on('enqueue', () => console.log(`Notification job created: ${job.id}`))
  .on('complete', () => console.log('Notification job completed'))
  .on('failed attempt', () => console.log('Notification job failed'));

job.save();
