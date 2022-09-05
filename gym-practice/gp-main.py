import gym

env = gym.make('CartPole-v1', render_mode="human", new_step_api=True)
env.action_space.seed(55)

#env.reset()
observation = env.reset(seed=55)
# init reward_sum
reward_sum = 0
# init epoch at year 0
epoch = 0
rewards_list = []

def sortRewardsList(obj):
  return obj["reward"]

for _ in range(200):
  observation, reward, terminated, truncated, info = env.step(env.action_space.sample())
  # increment reward_sum by reward
  reward_sum += reward
  print(reward_sum)
  # if epoch comes to an end via termination
  if terminated == True:
    # increase the age of the epoch
    rewards_list.append({"epoch": epoch, "reward": reward_sum})
    epoch += 1
    print('END')
    reward_sum = 0
    observation = env.reset()

rewards_list_sorted = rewards_list.sort(reverse=True, key=sortRewardsList)
print(rewards_list)

env.close()
