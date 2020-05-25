# -*- coding: utf-8 -*-
import numpy as np
from scipy.special import expit, logit
import matplotlib.pyplot as plt
import imageio
import json
cwd = "D:\\SpyderProjects\\Master_projects\\image\\"
file = open(cwd + 'myjson.json', 'r')
obj = json.load(file)
file.close()

class Network:
    scorecard = obj['scorecard']
    def __init__(self, input_nodes, hidden_nodes, out_nodes, learn_rate):
        self.inodes = input_nodes
        self.hnodes = hidden_nodes
        self.onodes = out_nodes

        self.lr = learn_rate

        self.wih = np.asarray(obj['wih'])
        self.who = np.asarray(obj['who'])

        self.activation_func = lambda x: expit(x)
        self.reactivation_func = lambda x: logit(x)

    def train(self, input_list, target_list):
        inputs = np.array(input_list, ndmin=2).T
        targets = np.array(target_list, ndmin=2).T

        hidden_inputs = np.dot(self.wih, inputs)
        hidden_outputs = self.activation_func(hidden_inputs)

        final_inputs = np.dot(self.who, hidden_outputs)
        final_outputs = self.activation_func(final_inputs)

        output_errors = targets - final_outputs
        hidden_errors = np.dot(self.who.T, output_errors)

        self.who += self.lr * np.dot((output_errors * final_outputs *
                                      (1.0 - final_outputs)),
                                     np.transpose(hidden_outputs))
        self.wih += self.lr * np.dot((hidden_errors * hidden_outputs *
                                      (1.0 - hidden_outputs)),
                                     np.transpose(inputs))

    def query(self, input_list):
        inputs = np.array(input_list, ndmin=2).T

        hidden_inputs = np.dot(self.wih, inputs)

        hidden_output = self.activation_func(hidden_inputs)

        final_inputs = np.dot(self.who, hidden_output)

        final_outputs = self.activation_func(final_inputs)

        return final_outputs

    def reverse_query(self, output_list):

        final_outputs = np.array(output_list, ndmin=2).T
        final_intputs = self.reactivation_func(final_outputs)

        hidden_outputs = np.dot(self.who.T, final_intputs)
        hidden_outputs -= np.min(hidden_outputs)
        hidden_outputs /= np.max(hidden_outputs)
        hidden_outputs *= 0.98
        hidden_outputs += 0.01

        hidden_inputs = self.reactivation_func(hidden_outputs)

        inputs = np.dot(self.wih.T, hidden_inputs)
        inputs -= np.min(inputs)
        inputs /= np.max(inputs)
        inputs *= 0.98
        inputs += 0.01

        return inputs

    def get(self, input_list):
        response = self.query(input_list)
        result = np.argmax(response)
        return result

    def initial_train(self):
        train_data_file = open('mnist_train.csv', 'r')
        train_data_list = train_data_file.readlines()
        train_data_file.close()
        epochs = 4
        for e in range(epochs):
            for record in train_data_list:
                all_values = record.split(',')
                inputs = (np.asfarray(all_values[1:]) / 255.0 * 0.99) + 0.01
                targets = np.zeros(output_nodes) + 0.01
                targets[int(all_values[0])] = 0.99
                self.train(inputs, targets)

    def initial_test(self):
        self.scorecard = []
        test_data_file = open('mnist_test.csv', 'r')
        test_data_list = test_data_file.readlines()
        test_data_file.close()
        for record in test_data_list:
            all_values = record.split(',')
            correct_label = int(all_values[0])
            inputs = (np.asfarray(all_values[1:])/255.0*0.99) + 0.01
            outputs = self.query(inputs)
            label = np.argmax(outputs)
            if label == correct_label:
                self.scorecard.append(1)
            else:
                self.scorecard.append(0)


if __name__ == '__main__':
    input_nodes, hidden_nodes, output_nodes, learning_rate = 784, 200, 10, 0.2
    n = Network(input_nodes, hidden_nodes, output_nodes, learning_rate)

    print("натыйжалуулук:", np.average(n.scorecard)*100, " %")

    cwd = 'C:\\Users\\soyuz\\Desktop\\'
    next_step = 'y'
    targets = np.zeros(output_nodes) + 0.01
    while next_step.upper() != 'N':
        img_array = imageio.imread(cwd + 'number.png', as_gray=True)
        img_data = 255.0 - img_array.reshape(784)
        img_data = (img_data / 255.0 * 0.99) + 0.01
        output = n.query(img_data)
        label = np.argmax(output)
        print('сүрөттөгү сан: ', label)
        targets[:] = 0.01
        if input('нейрондук тармак туура иштедиби? ').upper() != 'N':
            targets[int(label)] = 0.99
        else:
            true_answer = input('туурасын киргизиңиз? ')
            targets[int(true_answer)] = 0.99
        n.train(img_data, targets)

        next_step = input('кайталайбызбы? (y/n) ')
    obj['who'], obj['wih'] = n.who.tolist(), n.wih.tolist()
    obj['scorecard'], obj['score'] = n.scorecard, np.average(n.scorecard) * 100
    file = open(file.name, 'w+')
    json.dump(obj, file)
    file.close()
