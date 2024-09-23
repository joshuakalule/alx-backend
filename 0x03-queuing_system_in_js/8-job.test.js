import createPushNotificationsJobs from "./8-job";
import { createQueue } from 'kue';
import { expect } from "chai";

const queue = createQueue();

describe('createPushNotificationJobs', function () {
  before(function () {
    queue.testMode.enter(true);
  });

  afterEach(function () {
    queue.testMode.clear();
  });

  after(function () {
    queue.testMode.exit();
  });

  it('display a error message if jobs is not an array', function () {
    const jobs = 'not an array'
    expect(() => createPushNotificationsJobs(jobs, queue)).to.throw(Error, 'Jobs is not an array');
  });

  it('create two new jobs to the queue', function () {
    const lenBefore = queue.testMode.jobs.length
    const jobs = [
      { phoneNumber: '256787302678', message: 'Wheres my money man!' },
      { phoneNumber: '256787302678', message: 'Youve got money to buy glasses!' }
    ]
    createPushNotificationsJobs(jobs, queue);
    expect(queue.testMode.jobs.length).to.not.be.equal(lenBefore);
    expect(queue.testMode.jobs.length).to.be.equal(2);
    expect(queue.testMode.jobs[0].type).to.be.equal('push_notification_code_3');
  });
});
